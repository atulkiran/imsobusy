<template>
	<div class="todo-item" v-bind:class="{'is-complete':todo.completed}">
		<p>
			<input type="checkbox" v-bind:checked="todo.completed" v-on:change="markComplete">


			{{todo.title}}
			
            <button @click="$emit('del-todo', todo.id)" class="del">x</button>

		</p>
        <p>
            Due Date: {{todo.due_date}}
        </p>
	</div>

</template>

<script>
import axios from 'axios';
import utils from './utils';
const prepUrl = utils.prepUrl

	export default{
		name:"Todoitem",
		props: ["todo"],
		methods: {
			markComplete() {
				this.todo.completed = !this.todo.completed;
                
                axios.post(prepUrl('/toggle_todo'), {"todo_id":this.todo.id})
                .catch(err => console.log(err));
                

			}
		}
	}
</script>

<style scoped>
    .todo-item {
        background:#f4f4f4;
        padding: 10px;
        border-bottom: 1px #ccc dotted;
    }

    .is-complete {
        text-decoration: line-through;
    }

    .del{
        background:#ff0000;
        color:#fff;
        border: none;
        padding: 5px 9px;
        border-radius: 50%;
        cursor: pointer;
        float: right;

    }
</style>