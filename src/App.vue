<template>
  <div id="app">
    <div class = "header">
    <img id = "logo" alt="Game logo" src="./assets/logo.png">
    <h1 id = "Title">Game Scores</h1>
    </div>

    <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
@media only screen and (max-width: 900px) {
 #app {
 
  display: grid;
  grid-template-columns: 100%;
  grid-gap: 10px;
  background-color: #fff;
 color: #2c3e50;
}
}

@media only screen and (min-width:900px) {
    #app {
 
  
  display: grid;
  grid-template-columns: 250px calc(100vw - 250px);
  grid-gap: 10px;
  background-color: #fff;
  color: #2c3e50;
}
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

}
#logo{
 
 
}
.header{
 height:250px;
}
#Title{
  margin-bottom:40px;

}
</style>
