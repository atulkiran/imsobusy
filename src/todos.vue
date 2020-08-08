<template>
  <div id = "app">
    <AddTodo v-on:add-todo="addTodo"/>
    <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo "/>
  </div>
</template>