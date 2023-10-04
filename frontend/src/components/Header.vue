<template>
    
      <v-app-bar color="blue-darken-4">
    
        <v-app-bar-nav-icon 
          variant="text"
          @click.stop="drawer = !drawer">
        </v-app-bar-nav-icon>
        
        <v-app-bar-title class="title  font-weight-bold">
        MindMingle
        </v-app-bar-title>
        
        <v-app-bar-title class="subtitle  font-weight-bold">
            FeatureExtraction
        </v-app-bar-title>

        <template v-slot:append>
          <v-btn>
            Sign-In
          </v-btn>

          <v-btn>
            <v-icon>
              mdi-home
            </v-icon>
          </v-btn>
        </template>
        </v-app-bar>
        
        <v-navigation-drawer
            v-model="drawer"
        >
            <v-list>
            <v-list-item title="Home" value="home"></v-list-item>
            <v-list-item title="About" value="about"></v-list-item>
            </v-list>
        </v-navigation-drawer>
        
        
    
</template>
   

<script>
  export default {
    name: 'Header',
    data: () => ({
    drawer: null,
  }),
  }
</script>

<style scoped>

.title{
    font-family: 'Pacifico', sans-serif;
    font-size: 20px;
}

.subtitle{
    font-family:  sans-serif;
    font-size: 25px;
}

</style>