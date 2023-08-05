<script>
  import axios from 'axios';
  import Nav from './Nav.svelte';

  let videoUrl = '';

  const respone = async () => {
    const res = await axios({
      method: 'post',
      url: 'http://localhost:5000/',
      data: {
        videoUrl: videoUrl,
      },
    });
    console.log('videoURl', res.data);
  };
</script>

<Nav />
<div class="row">
  <div class="col">
    <input
      type="text"
      class="form-control"
      placeholder="URL Link"
      aria-label="First name"
      bind:value={videoUrl}
    />
  </div>
</div>
<button type="button" class="btn btn-outline-success" on:click={respone}
  >Success</button
>

<style>
  div {
    margin-top: 5px;
  }
</style>
