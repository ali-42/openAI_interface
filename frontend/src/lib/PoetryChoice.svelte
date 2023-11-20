<script lang="ts">
  export let currentPoetry: string = ''
  let poetries = [
    "Haiku",
    "Sonnet",
    "Acrostiche",
    "Ballade",
  ]
  const changePoetry = (poetry: any) => {
    currentPoetry = poetry.poetry.toLowerCase()
  }


</script>

<nav>
  {#each poetries as poetry}
  {#if poetry.toLowerCase() === currentPoetry}
    <button class="poetry-category current" on:click={() => changePoetry({poetry})}>{poetry}</button><br>
  {:else}
    <button class="poetry-category" on:click={() => changePoetry({poetry})}>{poetry}</button><br>
  {/if}
  {/each}
</nav>

<style>
  nav {
    display:flex;
    flex-direction:column;
    min-width: 300px;
    
  }

  .current {
    background-color:rgba(0, 0, 0, 0.2)
  }

  .poetry-category {
    height:100px;
  }

  button {
    border:none;
    font-size:2em;
    background-color:transparent;
  }
  
  button:hover {
    background-color:rgba(0, 0, 0, 0.1)
  }
</style>
