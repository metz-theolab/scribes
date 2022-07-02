<template>
  <b-container id="app">
    <b-row>
      <b-col class="text-center"> Gospel of John - Chapter 1 </b-col>
    </b-row>
    <b-row>
      <ManuscriptSelector
        v-for="manuscript in availableManuscripts"
        :key="manuscript"
        :ManuscriptID="manuscript"
      >
      </ManuscriptSelector>
    </b-row>
    <b-row>
      <b-col w="6">
        <b-button :pressed.sync="synopticSelected" variant="danger">
          Synoptic
        </b-button>

        <SynopticChoices></SynopticChoices>
      </b-col>

      <b-col w="6">
        <b-button :pressed.sync="collatedSelected" variant="danger">
          Collate
        </b-button>
        <b-checkbox v-if="collatedSelected" v-model="collapsed"
          >Collapsed</b-checkbox
        >
      </b-col>
    </b-row>
    <b-row class="justify-content-md-center">
      <CollationViewer
        v-if="collatedSelected & !collapsed"
        :collation="collation"
      ></CollationViewer>
      <CollapsedCollationViewer
        v-if="collatedSelected & collapsed"
        :collapsedCollation="collapsedCollation"
      ></CollapsedCollationViewer>
    </b-row>
  </b-container>
</template>

<script>
import ManuscriptSelector from "./components/ManuscriptSelector.vue";
import SynopticChoices from "./components/SynopticChoices.vue";
import CollationViewer from "./components/CollationViewer.vue";
import CollapsedCollationViewer from "./components/CollapsedCollationViewer.vue";

export default {
  name: "App",
  components: {
    ManuscriptSelector,
    SynopticChoices,
    CollationViewer,
    CollapsedCollationViewer,
  },
  data: function () {
    return {
      collapsed: false,
      synopticSelected: false,
      collatedSelected: false,
      availableManuscripts: ["MS1", "MS2", "MS3"],
      collapsedCollation: {
        Au: {},
        Commencement: {},
        Etait: {},
        La: { MS2: "le" },
        Parole: { MS2: "Verbe" },
      },
      collation: {
        MS1: {
          Au: "test lexic",
          commencement: "c'est le début",
          était: "ceci est un verbe !",
          la: "",
          parole: "ce qu'on prononce",
          ".": "",
        },
        MS2: {
          Au: "test lexic",
          commencement: "c'est le début",
          était: "ceci est un verbe !",
          le: "",
          Verbe: "ceci est une définition",
          ".": "",
        },
      },
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
