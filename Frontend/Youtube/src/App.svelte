<script>
  import Router from 'svelte-spa-router';
  import Download from './Download.svelte';

  let routes = {
    '/': Download,
  };
</script>

<main>
  <Router {routes} />
</main>
