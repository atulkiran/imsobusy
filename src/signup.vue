<template>
    <div class="vue-tempalte">
        <form @submit="adduser">
            <h3>Sign Up</h3>

            <div class="form-group">
                <label>First Name</label>
                <input type="text" v-model="first_name" name = "first_name" class="form-control form-control-lg"/>
            </div>

            <div class="form-group">
                <label>Last Name</label>
                <input type="text" v-model="last_name" name="last_name" class="form-control form-control-lg"/>
            </div>

            <div class="form-group">
                <label>Email address</label>
                <input type="email" v-model="email" name="email" class="form-control form-control-lg" />
            </div>

            <div class="form-group">
                <label>Password</label>
                <input type="password" v-model="password" name="password" class="form-control form-control-lg" />
            </div>

            <button type="submit" class="btn btn-dark btn-lg btn-block">Sign Up</button>

            <p class="forgot-password text-right">
                Already registered 
                <router-link :to="{name: 'login.vue'}">sign in?</router-link>
            </p>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
import utils from './utils';
const prepUrl = utils.prepUrl

    export default {
        name: "AddUser",
        data() {
            return {
                first_name:"",
                last_name:"",
                email:"",
                password:"",



            }
        },


        methods:{
            adduser(e) {
                e.preventDefault();
                const new_user = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    password: this.password};

                    const {first_name, last_name, email, password} = new_user;

                    axios.post(prepUrl('/signup'), {first_name, last_name, email, password})
        .then(res => this.users = [...this.users, res.data])
        .catch(err => console.log(err));

        console.log(new_user)



    
                },
            }
        }
    
</script>

