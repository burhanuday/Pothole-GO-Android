const mongoose = require("mongoose");
const { Schema } = mongoose;

const userSchema = new Schema({
  username: {
    type: String,
    index: true,
    dropDups: true,
    required: true
  },
  email: {
    type: String,
    unique: true,
    required: true
  }
});

const User = mongoose.model("User", userSchema);
module.exports = User;
