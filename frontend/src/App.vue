<template>
  <div id="app">
    <form @submit.prevent="createTweet">
      <div class="form-group row">
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Name"
          v-model="tweet.name"
        >
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Message"
          v-model="tweet.message"
        >
        <button class="btn btn-success">Tweet</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Time</th>
        <th>Message</th>
        <th>Name</th>
      </thead>
      <tbody>
        <tr
          v-for="tweet in tweets"
          :key="tweet.id"
        >
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
  margin-top: 60px;
}
</style>
