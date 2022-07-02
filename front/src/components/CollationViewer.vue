<template>
  <b-col w="12">
    <div v-for="(content, manuscript) in collation" :key="content">
      <b-button pill variant="info">{{ manuscript }}</b-button>
      <span v-for="(analysis, word) in content" :key="word">
        <span v-b-tooltip.hover :title="analysis"> {{ word }}</span>
      </span>
    </div>
  </b-col>
</template>

<script>
export default {
  name: "CollationViewer",
  props: {
    collation: Object,
  },
};
</script>
