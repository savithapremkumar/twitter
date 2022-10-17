<template>
  <div id="app">
    <h4 class="mb-5">Hey visitor, feel free to tweet!</h4>
    <form @submit.prevent="createTweet" class="mb-4">
      <div class="form-group row">
        <div class="col">
          <input
            type="text"
            class="form-control col-3 mx-2"
            placeholder="Name"
            v-model="tweet.name"
          />
        </div>
        <div class="col">
          <input
            type="text"
            class="form-control col-3 mx-2"
            placeholder="Message"
            v-model="tweet.message"
          />
        </div>
        <div class="col">
          <button class="btn btn-success">Submit Tweet</button>
        </div>
      </div>
    </form>

    <table class="table table-striped table-bordered">
      <thead>
        <th>Time</th>
        <th>Message</th>
        <th>Name</th>
      </thead>
      <tbody>
        <tr v-for="tweet in tweets" :key="tweet.id">
          <td>{{ tweet.datetime }}</td>
          <td>{{ tweet.message }}</td>
          <td>{{ tweet.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      tweet: {
        datetime: "",
        message: "",
        name: "",
      },
      tweets: [],
    };
  },

  async created() {
    await this.getTweets();
  },
  methods: {
    async getTweets() {
      var response = await fetch("http://localhost:8000/api/tweets/");
      this.tweets = await response.json();
    },
    async createTweet() {
      await this.getTweets();
      await fetch("http://localhost:8000/api/tweets/", {
        method: "post",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.tweet),
      });
      await this.getTweets();
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px 60px 0 60px;
}
</style>
