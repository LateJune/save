# save
Save things quickly from command line. Useful for quick notes or storing an entire ssh or bash session and finding stuff you did.
By default it will append to ~/savefile with a timestamp.

Add this to your `~/.bashrc` to use:

`PROMPT_COMMAND="history -a;$PROMPT_COMMAND"`

Run this command or start a new shell:

`source ~/.bashrc`

### How to use save
`save` to store the most recent command in the current terminal`
- TODO: make this work with an aborted command (CTRL+C)

`save literally any text`
- Saves the text

`save -i "a command"`
- Saves the program name itself and any output.
- Works with interactive programs like `bash -i`, or `ssh`.

`save -p savefile "search string"`
- looks for `string` in the list of commands and will print output.
- For example `save -p sshsave nmap` will return every instance of nmap from a saved ssh session.

