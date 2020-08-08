<template>
	<div>
		<form @submit="addTodo">
			<input type="text" v-model="title" name="title" placeholder="Add Todo...">
			<input type="date" v-model="due_date" name="due_date" placeholder="Enter Due Date....">
			<input type="submit" value="Submit" class="btn">
		</form>
	</div>
	
</template>

<script>
	//import uuid from 'uuid';
	export default {
		name: "AddTodo",
		data() {
			return {
				title:'',
				due_date:'',
			}
		},
		methods: {
			addTodo(e) {
				e.preventDefault();
				const newTodo = {
					description: this.title,
					due_date: this.due_date,
					completed: false
				}
				// send up to parent
				this.$emit('add-todo', newTodo);

				this.title = '';
			}
		}
	}
	
</script>

<style scoped>
  form {
    display: flex;
  }

  input[type="text"] {
    flex: 10;
    padding: 5px;
  }

  input[type="submit"]{
    flex:2;
  }
</style>