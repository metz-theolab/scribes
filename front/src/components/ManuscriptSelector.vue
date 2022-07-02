<template>
  <b-row>
    <b-col w="1">
      <b-button
        variant="outline-primary"
        v-for="manuscript in manuscriptLists"
        label="manuscript"
        :key="manuscript"
        >{{ manuscript }}</b-button
      >
    </b-col>
  </b-row>
</template>

<script>
export default {
  name: "ManuscriptSelector",
  props: {
    manuscriptLists: Array,
  },
  //   data() {
  //     return {
  //       manuscriptLists: ["Shanghai", "Beijing", "Guangzhou", "Shenzhen"],
  //     };
  //   },
};
</script>
