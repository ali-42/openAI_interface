<script lang='ts'>
  import Poetry from "$lib/Poetry.svelte";
  import PoetryChoice from "$lib/PoetryChoice.svelte";
  import { logged } from "$lib/stores";
  import { goto } from "$app/navigation";

  let currentPoetry: string = ""

  const login = () => {
    goto('/login')
  }

</script>

{#if $logged}

<div>

<PoetryChoice bind:currentPoetry/>

  {#if currentPoetry !== ''}
  <div class="chat">
    <Poetry bind:poetry={currentPoetry} />
  </div>
  {/if}

</div>

{:else}
<div class="authenticate">
  <button class="authenticate" on:click={login}>authenticate</button>
</div>
{/if}


<style>
  div {
    display:flex
  }

  .chat {
    padding-left:1em; 
    padding-top:1em; 
    background-color:lightgrey;
    flex:1;
  }

  .authenticate {
    font-size: 1.2em;
    margin: 0.5em;
    margin:auto;
    margin-top:2em;
    padding: 0.5em;
  }


</style>
