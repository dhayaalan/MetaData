<script>
  import axios from 'axios';
  import Nav from './Nav.svelte';
  import { onMount } from 'svelte';
  export let width = 30;

  let items = [];

  const fetchVideos = async () => {
    try {
      const response = await axios({
        method: 'get',
        url: 'http://localhost:5000/list',
      });
      console.log(response.data);
      items = response.data;
    } catch (error) {
      console.error('Error fetching video data:', error);
    }
  };

  // Function to replace slashes with underscores
  function replaceSpacesAndEncode(filename) {
    return encodeURIComponent(filename.replace(/ + /g, ' '));
  }

  onMount(fetchVideos);
</script>

<Nav />
<div class="div">
  {#each items as item}
    <!-- <div class="div"> -->
    <div class="card" style="width: {width}%;">
      <div class="card-body">
        <h5 class="card-title">{item.title}</h5>
        <p class="card-text">{item.url}</p>
        <div class="embed-responsive embed-responsive-16by9">
          <video class="embed-responsive-item" controls>
            <source
              type="video/mp4"
              src={`http://localhost:5000/video/${replaceSpacesAndEncode(
                item.filename
              )}`}
            />
            Your browser does not support the video tag.
            <track kind="captions" />
          </video>
        </div>
      </div>
    </div>
  {/each}
</div>
