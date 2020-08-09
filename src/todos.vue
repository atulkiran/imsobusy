<template>
  <div id = "app">

    <AddTodo v-on:add-todo="addTodo"/>

    <div v-bind:key="index" v-for="(todo, index) in todos">
      <Todoitem v-bind:todo="todo" v-on:del-todo="deleteTodo(todo.id)"/>
    </div>

    <h4 v-if="todos.length == 0">
    Oh, the weather outside is crummy,
    and you feel as lively as a mummy,
    then there's nothing to do or say;
    it's 'There's Nothing to Do Today Day'.
    Don't you know, when there's nothing to do
    you can do anything that you want to.
    You can go to sleep, run and play
    on There's Nothing to Do, Nothing to Do Today Day. (Nothing to Do Today Day)
    Nothing to Do Today Day (Nothing to Do Today Day)
    Nothing to Do Today Day-aaaay!</h4>

    <video v-if="todos.length == 0" width="320" height="240" autoplay="autoplay" muted controls>
      <source src="/img/nothing2do.mov" type="video/mp4">
    </video>
    <div>
      <input type="checkbox" v-model="show_completed" v-on:change="toggle_completed">
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import Todoitem from './Todoitem.vue'
import AddTodo from './AddTodo.vue'
import utils from './utils';
const prepUrl = utils.prepUrl

export default {
  name: 'todos',
  components: {
    AddTodo,
    Todoitem,
  },
  data() {
    return {
      todos : [],
      show_completed: false,
    }
  },
  methods: {
    deleteTodo(id) {
      axios.post(prepUrl('/delete'), {"todo_id": id})
        .then(() => this.todos = this.todos.filter(todo => todo.id !== id))
        .catch(err => console.log(err));
    },
    addTodo(newTodo) {
      const {description, due_date, completed} = newTodo;
      axios.post(prepUrl('/newtodo'), {description, due_date, completed})
        .then(res => this.todos = [...this.todos, res.data])
        .catch(err => console.log(err));
    },
    toggle_completed(){
      let x = ""
      if (!this.show_completed) {
          x = '?completed=false'
      } else {
          x = '?completed=true'
      }
      axios.get(prepUrl('/gettodos') + x)
        .then(res => this.todos = res.data.all_todos)
        .catch(err => console.log(err));
    }
  },
  created() {
    axios.get(prepUrl('/gettodos'))
      .then(res => this.todos = res.data.all_todos)
      .catch(err => console.log(err));
  }
}

</script>

<style>

</style>