<template>
  <div>
    <b-row>
      <b-col w="6" v-for="(content, manuscript) in collation" :key="content">
        <b-button v-b-toggle.sidebar-1 pill variant="info">{{
          manuscript
        }}</b-button>
        <span v-for="(analysis, word) in content" :key="word">
          <span v-b-popover.hover.top :title="analysis"> {{ word }}</span>
        </span>
      </b-col>
    </b-row>
    <b-sidebar id="sidebar-1" title="Sidebar" shadow>
      <div class="px-3 py-2">
        <p>This is the best manuscript ever !</p>
        <b-img
          src="https://picsum.photos/500/500/?image=54"
          fluid
          thumbnail
        ></b-img>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
export default {
  name: "SynopticViewer",
  props: {
    collation: Object,
  },
};
</script>
