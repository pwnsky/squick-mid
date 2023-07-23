module.exports = {
  webpackBarName: 'vue-admin-better',
  webpackBanner:
    ' build: this project build by vue-admin-beautiful ',
  donationConsole() {
    const chalk = require('chalk')
    console.log(
      chalk.green(
        `> github：https://github.com/chuzhixin/vue-admin-beautiful`
      )
    )
  },
}
