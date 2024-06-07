<template>
  <div>
    <v-app>
      <Header></Header>
      <Text ref="Text" v-if="loading === false"></Text>
      <Form @dataSubmitted="dataSubmitted"></Form>
    </v-app>
  </div>
</template>
  
<script>
import Text from './components/Text_display.vue'
import Header from './components/Header.vue'
import Form from './components/Text_form.vue';
export default {
  data() {
    return {
      showComponent: true,
      loading: false,
    };
  },
  components: {
    Text,
    Header,
    Form,
  },
  methods: {
    dataSubmitted() {
      this.loading = true;
      setTimeout(() => {
        this.$refs.Text.fetchResult();
      }, 1000);
      this.reloadComponent();
    },
    reloadComponent() {
      this.$nextTick(() => {
        this.loading = false;
      });
    }
  }
}
</script>
  
<style>
.my-fonts {
  font-family: Arial, sans-serif;
}
</style>
