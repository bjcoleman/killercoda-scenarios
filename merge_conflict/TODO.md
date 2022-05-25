
## TODO

* Write the text for the steps (Coleman)
* Retry on create repo/conflict
  * Need to document behavior of containers
  * Need to have the katacoda foreground and background scripts handle response
  * Add a block on the first "Continue" button if it fails
* Write to folder other that `/root` with `repo_name` file
* Figure out how to have the user add their name/email (right now it uses a Katacaoda name/email by default)
  * IDEA: include text that states what it will do by default and provide the `git config` commands to change it if they want.
  * IDEA: In the create_repo script, add `input` statements for name/email, and then write the values to `.gitconfig`
* In create_repo and create_conflict Docker containers, set the username and email of the committer when we add commits. (Jacob)
* Change the bash prompt to display information about the git repo.
* Make conflict using a PR (rather than directly into `upstream`)
* How many adjectives and nouns are there?  This determines the probability
of getting a duplicate repo name.  The `create_repo` container should check
if the repo already exists and generate a new name.


## Annoyances

* Scenario runs as root.  Is there a way to run as a non-root user?
  * Can a paid user create a DOCKER image that uses a different (non-root) user?

## Future Work

* After the user forks and clones the repo, add more content to upstream.  When the user does a `git pull upstream main` they will get additional changes.
* After the user clones, add git hooks to protect them from mistakes (similar to what Karl does)
