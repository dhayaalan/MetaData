<script>
  import Router from 'svelte-spa-router';
  import Download from './Download.svelte';
  import List from './List.svelte';

  let routes = {
    '/': Download,
    '/list': List,
  };
</script>

<main>
  <Router {routes} />
</main>
