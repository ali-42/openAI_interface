<script lang="ts">
  import { logged } from "./stores";
  
  const logout = () => {
      logged.set(0)
  }

</script>



<nav>
  <a href="/">Home</a>
  {#if $logged}
  <a href="/login" on:click={logout}>logout</a>
  {:else}
  <a href="/login">login</a>
  {/if}
</nav>
