<h1>
    <p align="left">
        <a href="t.me/rmprojects">മൊഴി (Mozhi)</a>
    </p>
</h1>
<h3>
Mozhi (മൊഴി) is an English to Malayalam language translation telegrm bot.
</h3>
<p align="left">
Mozhi converts English words to Malayalam using Google Translation Library. It is a simple bot that can be used in any chat or by privately.
മൊഴി ഒരു ഇംഗ്ലീഷ് - മലയാളം മൊഴിമാറ്റ ടെലെഗ്രാം ബോട്ട് ആണ്. ഇൻലൈൻ ആയിട്ടാണ് ഇത് പ്രവർത്തിക്കുന്നത്.എല്ലാ ചാറ്റുകളിലും അല്ലെങ്കിൽ വ്യക്തിപരം ആയും ഇതിനെ ഉപയോഗിക്കാവുന്നതാണ്. 
    </p>
<h4>
Requirements:</h4>
<ul>
        <li><s>The Bot need to be in inline mode</s></li>
        <li><code>API_HASH</code>    -   Your API Hash from <a href="https://my.telegram.org">my.telegram.org</a></li>
        <li><code>APP_ID</code>      -   Your APP ID from <a href="https://my.telegram.org">my.telegram.org</a></li>
        <li><code>BOT_TOKEN</code>   -   Your bot token from <a href="https://telegram.dog/botfather">@BotFather</a></li>
</ul>
<br>
<p align="left">
    <a href="https://choosealicense.com/licenses/gpl-3.0/">
        <img src="https://img.shields.io/badge/License-GPLv3-blueviolet?style=for-the-badge&logo=gplv3">
    </a>
</p>
<p align="left"></p>
<h4>
Deploy -VPS:</h4>
    <ul>
        <li><strong>Open a Linux Terminal and Run the below commands ( Stage: 1 )</strong></li>
        <li><code>git clone https://github.com/m4mallu/mozhi</code></li>
        <li><code>cd mozhi</code></li>
        <li>Create a <code>config.py</code> with the Mandatory variables.</li>
        <li><strong>Run the below commands in the same terminal ( Stage: 2 )</strong></li>
        <li><code>virtualenv -p python3 venv</code></li>
        <li><code>. ./venv/bin/activate</code></li>
        <li><code>pip3 install -r requirements.txt</code></li>
        <li><code>python3 bot.py</code></li>
    </ul>
<h4>
Deploy - Heroku:</h4>
    <a href="https://heroku.com/deploy?template=https://github.com/m4mallu/mozhi">
        <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
    </a>
