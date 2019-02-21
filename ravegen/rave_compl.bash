#/usr/bin/env bash
Commands="help init create deploy change deleteCloudBot "
_completions()
{
if [ "${#COMP_WORDS[@]}" == "2" ]; then
COMPREPLY=($(compgen -W "$Commands" "\"${COMP_WORDS[1]}\""))
fi
if [ "${#COMP_WORDS[@]}" != "2" ]; then
if [ "${COMP_WORDS[1]}" == "deploy" ]; then
COMPREPLY=($(compgen -W "-t -d " "\"${COMP_WORDS[-1]}\""))
fi
if [ "${COMP_WORDS[1]}" == "create" ]; then
COMPREPLY=($(compgen -W "-t -d " "\"${COMP_WORDS[-1]}\""))
fi
if [ "${COMP_WORDS[1]}" == "init" ]; then
COMPREPLY=($(compgen -W "-m " "\"${COMP_WORDS[-1]}\""))
fi
if [ "${COMP_WORDS[1]}" == "change" ]; then
COMPREPLY=($(compgen -W "-t -d " "\"${COMP_WORDS[-1]}\""))
fi
fi
}

complete -F _completions ravegen