<script>
  import Nav from './Nav.svelte';
</script>

<Nav />
<div class="row">
  <div class="col">
    <input
      type="text"
      class="form-control"
      placeholder="URL Link"
      aria-label="First name"
    />
  </div>
</div>
<button type="button" class="btn btn-outline-success">Success</button>

<style>
  div {
    margin-top: 5px;
  }
</style>
