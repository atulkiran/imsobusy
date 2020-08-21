<template>
 <div class="TheLogin">
        <form>
            <h3>Sign In</h3>

            <div class="form-group">
                <label>Email address</label>
                <input type="email" class="form-control form-control-lg" />
            </div>

            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control form-control-lg" />
            </div>

            <button type="submit" class="btn btn-dark btn-lg btn-block">Sign In</button>

            <p class="forgot-password text-right mt-2 mb-4">
                <router-link to="/forgot">Forgot password ?</router-link>
            </p>

            <p class="signup text-right mt-2 mb-4">
                <router-link to="/signup">Not a Member? Signup!</router-link>
            </p>

        
        </form>
    </div>
</template>

<script>
    export default {}
 
</script>

