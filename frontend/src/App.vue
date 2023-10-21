<template>
    <div>
      <v-app>
        <Header></Header>
        <Text></Text>
        <Form></Form>
      </v-app>
    </div>
  </template>
  
  <script>
  import Text from './components/Text_display.vue'
  import Header from './components/Header.vue'
  import Form from './components/Text_form.vue';
  export default {
    components: {
      Text,
      Header,
      Form,
    }
  }
  </script>
  
<style>
  .my-fonts {
    font-family: Arial, sans-serif;
  }
</style>
