<script lang="ts">
import Navbar from "$lib/Navbar.svelte";
import HeadTitle from "$lib/HeadTitle.svelte";
import { logged } from "$lib/stores";

</script>

{#if $logged }
  <Navbar />
  <HeadTitle />
{/if}

<slot />

