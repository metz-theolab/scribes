<template>
  <b-col w="12">
    <span v-for="(variants, content) in collapsedCollation" :key="content">
      <span v-if="Object.keys(variants).length != 0">
        <span v-for="(variant, value) in variants" :key="variant">
          <b-button
            variant="outline"
            v-b-tooltip.hover
            :title="value + ': ' + variant"
          >
            {{ content }}
          </b-button>
        </span>
      </span>
      <span v-else> {{ content }} </span>
    </span>
  </b-col>
</template>

<script>
export default {
  name: "CollapsedCollationViewer",
  props: {
    collapsedCollation: Object,
  },
  methods: {
    variantList(manuscript, value) {
      return manuscript + value;
    },
  },
};
</script>
