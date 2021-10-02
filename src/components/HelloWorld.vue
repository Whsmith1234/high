<template>
  <div class="hello">
   
    <ul class ="wrapper" id="User List">
      <div id = "winner" class ="box" v-for="User in Highest" :key="User.username">
        <h3>HighScore</h3> 
        {{ User.name }} <br>
        <img :src = "User.imageUrl">
        <br>
        Score: {{User.score}}
      </div>
      <div class ="box" v-for="User in Users" :key="User.username">
        <h3>Regular</h3> 
        {{ User.name }} <br>
        <img :src = "User.imageUrl">
        <br>
        Score: {{User.score}}
      </div>
      
    </ul>
  </div>
 
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
     Highest:[
     ],
     Users:[],
  }
  },
  created () {
       
        this.timer = setInterval(this.fetchUserList, 1000);  
    },
    methods: {
        fetchUserList () {
          
            fetch('https://wpra.pythonanywhere.com/')
  .then(response => response.json())
  .then(data => {
      var max =0;
      var Users=data;
      var regular =[];
      var high = [];
          for(var user in Users){
              if(Users[user].score>max){
                for(var i in high){
                 regular.push(high[i]);
                }
                high=[];
                high.push(Users[user]);
                max = Users[user].score;

              }else if(Users[user].score==max){
                high.push(Users[user]);
              }else{
                regular.push(Users[user]);
              }
              
          }
          this.Users= regular;
          this.Highest = high;
        });
            
},
  },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
body {
  margin: 40px;
}
h3{
  margin-top:0;
  margin-bottom:0;
}
.wrapper{
  width:90%;
  margin-left:auto;
  margin-right:auto;
  display: grid;
  background-color: #fff;
  color: #2c3e50;
  grid-gap: 10px;
}
@media only screen and (max-width: 600px) {
 .wrapper {
  grid-template-columns: 100%;
}
}
@media only screen and (max-width:900px) and (min-width:600px) {
    .wrapper {
  grid-template-columns: 50% 50%;
}
}
@media only screen and (min-width:900px) {
    .wrapper {
  margin-top:5px;
  grid-template-columns: 33% 33% 33%;
}
}
img{
  width:100px;
}
#winner{
  background-color:#42b983;
}
.box {
  background-color:#2c3e50;
  color: #fff;
  border-radius: 5px;
  padding: 20px;
  font-size: 150%;
}
</style>
