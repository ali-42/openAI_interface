<script lang='ts'>
  import { logged } from "./stores";
  import { currentUser } from "./stores";
  import axios from 'axios'
  import { goto } from "$app/navigation";

  let username = ''
  let password = ''
  let error = ''

    const logIn = async () => {
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password', password);

      try {
        const res = await axios.post('http://127.0.0.1:8000/auth/token', formData);
        if (res.status === 200) {
          logged.set(1) 
          localStorage.setItem("access_token", res.data[0].access_token);
          localStorage.setItem("refresh_token", res.data[1].access_token);
          axios.defaults.headers.common['Authorization'] = `Bearer ${res.data[0].access_token}`
          const getUsername = await axios.get('http://127.0.0.1:8000/', {withCredentials: true})
          if (getUsername.status === 200)
            currentUser.set(getUsername.data.User.username)
          goto('/')
        }
      }
      catch (e) {
        error = 'username does not exist or password does not match'
      }
    }

</script>

<form on:submit|preventDefault={logIn}>
  <input type="text" placeholder="username" bind:value={username}/>
  <input type="password" placeholder="password" bind:value={password}/>
  <button type="submit">sign in</button>
{#if error !== ''}
  <p class="error">{error}</p>
{/if}
</form>

<style>
input {
  font-size: 1.2em;
  text-align:center;
}

button {
  width: 5em;
  font-size: 1em;
  height:2em;
  margin:auto
}

form {
  margin:auto;
  margin-top:2em;
  display: flex;
  flex-direction: column;
  gap: 0.5em;
  max-width: 20em;
}

.error {
  color: red;
  text-align: center 
}

</style>
