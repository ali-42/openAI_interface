<script lang="ts">
    import { goto } from "$app/navigation";
    import { logged } from "$lib/stores";

    const login = () => {
      logged.set(1)
      goto('/')
    }
</script>

<button on:click={login}>login</button>


