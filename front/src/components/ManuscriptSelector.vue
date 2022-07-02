<template>
  <b-col w="1">
    <b-button pill variant="info">{{ ManuscriptID }}</b-button>
  </b-col>
</template>

<script>
export default {
  name: "ManuscriptSelector",
  props: {
    ManuscriptID: String,
  },
};
</script>
