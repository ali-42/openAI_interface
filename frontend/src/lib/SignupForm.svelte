<script lang='ts'>
  import { logged } from "./stores";
  import axios from 'axios'
  import { goto } from "$app/navigation";

  let username = ''
  let password = ''
  let error = ''

    const signUp = async () => {
      try {
        const res = await axios.post('http://127.0.0.1:8000/auth/', {
          username: username,
          password: password
        });
        if (res.status === 200)
          logged.set(1)
          goto('/')
      }
      catch (e) {
        console.log(e)
      }
    }

</script>

<form on:submit|preventDefault={signUp}>
  <input type="text" placeholder="username" bind:value={username}/>
  <input type="password" placeholder="password" bind:value={password}/>
  <button type="submit">sign up</button>
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
