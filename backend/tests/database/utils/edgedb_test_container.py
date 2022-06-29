"""Test container for EdgeDB."""

import edgedb
from edgedb import ClientConnectionClosedError
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_container_is_ready
import os

from pathlib import Path


CURRENT_DIR = Path(__file__).parent.absolute()
DB_SCHEMA = CURRENT_DIR / "dbschema" 



class EdgeDBContainer(DockerContainer):
    """EdgeDB test container."""

    def __init__(self, exposed_port: int = 5656, database_name: str = "scribes") -> None:
        """
        Initialize a test container on port exposed_port.

        Args:
            exposed_port (int): The port to expose.
                Defaults to 5656. 
        """
        super(EdgeDBContainer, self).__init__(
            image="edgedb/edgedb",
            docker_client_kw={},
        )
        self.edge_db_port = exposed_port
        self.database_name = database_name
        self.volumes[DB_SCHEMA] = {"bind": "/dbschema", "mode": "rw"}
        self.with_env("EDGEDB_SERVER_SECURITY", "insecure_dev_mode")
        self.with_exposed_ports(exposed_port)

    def start(self):
        """Starting the container."""
        super().start()
        os.environ["EDGEDB_CLIENT_SECURITY"] = "insecure_dev_mode"
        self._wait_database_ready()
        return self

    @wait_container_is_ready(ClientConnectionClosedError)
    def _wait_database_ready(self) -> None:
        """Testing the connection."""
        client = edgedb.create_client(dsn=self.get_edgedb_dsn("edgedb"), timeout=1)
        client.ensure_connected()
        client.close()

    def get_edge_db_host(self) -> str:
        """Get the edge db host.

        Returns:
            str: The host of the edge db host.
        """
        return self.get_container_host_ip()

    def get_edge_db_port(self) -> int:
        """Get the edge db port.

        Returns:
            int: The port of the edge db instance.
        """
        return self.edge_db_port
        
    def get_edge_db_name(self) -> str:
        """Get the name of the edge db database.

        Returns:
            str: The name of the database.
        """
        return self.database_name

    def get_edgedb_dsn(self, database_name: str) -> str:
        """DSN to specify connection information to EdgeDB for database database_name.
        
        Args:
            database_name (str): The name of the database.
        """
        return f"edgedb://edgedb:edgedb@{self.get_edge_db_host()}:" \
               f"{self.get_edge_db_port()}/{self.get_edge_db_name()}"