<script lang='ts'>
  import Sport from "$lib/Sport.svelte";

  let currentSport: string = ""
  let sports = [
    "Tennis",
    "Volleyball",
    "Rugby",
    "Football",
    "Cyclisme"
  ]


  const changeSport = (sport: any) => {
    currentSport = sport.sport.toLowerCase()
    console.log(currentSport)

  }


</script>

<div>
  <nav>
    {#each sports as sport}
    {#if sport.toLowerCase() === currentSport}
      <button class="sport-category current" on:click={() => changeSport({sport})}>{sport}</button><br>
    {:else}
      <button class="sport-category" on:click={() => changeSport({sport})}>{sport}</button><br>
    {/if}
    {/each}
  </nav>
  {#if currentSport !== ''}
  <div class="chat">
    <Sport bind:sport={currentSport} />
  </div>
  {/if}
</div>

<style>
  div {
    display:flex
  }

  nav {
    display:flex;
    flex-direction:column;
    min-width: 300px;
    
  }

  .current {
    background-color:rgba(0, 0, 0, 0.2)
  }

  .chat {
    padding-left:1em; 
    padding-top:1em; 
    background-color:lightgrey;
    flex:1;
  }

  .sport-category {
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
