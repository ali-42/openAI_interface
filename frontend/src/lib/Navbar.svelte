<script lang="ts">
  import { logged } from "./stores";
  
  const logout = () => {
      logged.set(0)
  }

</script>



<nav>
  {#if $logged}
  <a href="/login" on:click={logout}>logout</a>
  {:else}
  <a href="/login">login</a>
  {/if}
</nav>
