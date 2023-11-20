<script lang="ts">
    import LoginForm from "$lib/LoginForm.svelte";
    import SignupForm from "$lib/SignupForm.svelte";
    let option = ''

    const signIn = () => {
      option = 'signin'
    }

    const signUp = () => {
      option = 'signup'
    }

</script>


{#if option !== ''}
{#if option === 'signin'}
  <LoginForm />
{:else}
  <SignupForm />
{/if}
{:else}
<div>
  <button on:click={signIn}>sign in</button>
  <button on:click={signUp}>sign up</button>
</div>
{/if}

<style>
  div {
    text-align:center;
    margin-top:2em;
  }

  button {
    font-size: 1.1em;
    padding: 0.5em;
    margin: 0.5em;
  }
</style>
