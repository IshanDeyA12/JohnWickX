from bot import CMD_INDEX
import os
def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command


class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand(f'START_COMMAND', f'start2{CMD_INDEX}')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', f'mirror2{CMD_INDEX}')
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', f'unzipmirror2{CMD_INDEX}')
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', f'zipmirror2{CMD_INDEX}')
        self.CancelMirror = getCommand('CANCEL_COMMAND', f'cancel2{CMD_INDEX}')
        self.CancelAllCommand = getCommand('CANCEL_ALL_COMMAND', f'cancelall2{CMD_INDEX}')
        self.ListCommand = getCommand('LIST_COMMAND', f'list2{CMD_INDEX}')
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'search2{CMD_INDEX}')
        self.StatusCommand = getCommand('STATUS_COMMAND', f'status2{CMD_INDEX}')
        self.AuthorizedUsersCommand = getCommand('USERS_COMMAND', f'users2{CMD_INDEX}')
        self.AuthorizeCommand = getCommand('AUTH_COMMAND', f'authorize2{CMD_INDEX}')
        self.UnAuthorizeCommand = getCommand('UNAUTH_COMMAND', f'unauthoriz2e{CMD_INDEX}')
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', f'addsudo2{CMD_INDEX}')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', f'rmsudo2{CMD_INDEX}')
        self.PingCommand = getCommand('PING_COMMAND', f'ping2{CMD_INDEX}')
        self.RestartCommand =  getCommand('RESTART_COMMAND', f'restart2{CMD_INDEX}')
        self.StatsCommand = getCommand('STATS_COMMAND', f'stats2{CMD_INDEX}')
        self.HelpCommand = getCommand('HELP_COMMAND', f'help2{CMD_INDEX}')
        self.LogCommand = getCommand('LOG_COMMAND', f'log2{CMD_INDEX}')
        self.CloneCommand = getCommand('CLONE_COMMAND', f'clone2{CMD_INDEX}')
        self.CountCommand = getCommand('COUNT_COMMAND', f'count2{CMD_INDEX}')
        self.WatchCommand =  getCommand('WATCH_COMMAND', f'watch2{CMD_INDEX}')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', f'zipwatch2{CMD_INDEX}')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', f'qbmirror2{CMD_INDEX}')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_COMMAND', f'qbunzipmirror2{CMD_INDEX}')
        self.QbZipMirrorCommand = getCommand('QBZIP_COMMAND', f'qbzipmirror2{CMD_INDEX}')
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'del2{CMD_INDEX}')
        self.ShellCommand = getCommand('SHELL_COMMAND', f'shell2{CMD_INDEX}')
        self.ExecHelpCommand = getCommand('EXEHELP_COMMAND', f'exechelp{2CMD_INDEX}')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', f'leechset2{CMD_INDEX}')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', f'setthumb2{CMD_INDEX}')
        self.LeechCommand = getCommand('LEECH_COMMAND', f'leech2{CMD_INDEX}')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', f'unzipleech2{CMD_INDEX}')
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', f'zipleech2{CMD_INDEX}')
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', f'qbleech2{CMD_INDEX}')
        self.QbUnzipLeechCommand = getCommand('QBZIPLEECH_COMMAND', f'qbunzipleech2{CMD_INDEX}')
        self.QbZipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', f'qbzipleech2{CMD_INDEX}')
        self.LeechWatchCommand =getCommand('LEECHWATCH_COMMAND',  f'leechwatch2{CMD_INDEX}')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', f'leechzipwatch2{CMD_INDEX}')
        self.RssListCommand = getCommand('RSSLIST_COMMAND', f'rsslist2{CMD_INDEX}')
        self.RssGetCommand = getCommand('RSSGET_COMMAND', f'rssget2{CMD_INDEX}')
        self.RssSubCommand = getCommand('RSSSUB_COMMAND', f'rsssub2{CMD_INDEX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_COMMAND', f'rssunsub2{CMD_INDEX}')
        self.RssSettingsCommand = getCommand('RSSSET_COMMAND', f'rssset2{CMD_INDEX}')
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'
        self.AddleechlogCommand = getCommand('ADDLEECHLOG_COMMAND', f'addleechlog{CMD_INDEX}')
        self.RmleechlogCommand = getCommand('RMLEECHLOG_COMMAND', f'rmleechlog{CMD_INDEX}')

BotCommands = _BotCommands()
