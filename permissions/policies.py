class PermissionPolicy:
    """
    Static rules for allowed and forbidden actions.
    """

    # Absolutely forbidden (never auto-execute)
    FORBIDDEN_COMMANDS = [
        "rm -rf /",
        "shutdown",
        "reboot",
        "mkfs",
        ":(){ :|:& };:",  # fork bomb
    ]

    # Commands requiring explicit approval
    RESTRICTED_COMMANDS = [
        "sudo",
        "apt install",
        "pip install",
        "dd ",
        "mount",
        "umount",
    ]

    SAFE_ACTIONS = {
        "wifi",
        "audio",
        "open_url",
        "search",
        "app",
        "file_read",
    }

    @classmethod
    def is_forbidden(cls, text: str) -> bool:
        return any(cmd in text for cmd in cls.FORBIDDEN_COMMANDS)

    @classmethod
    def is_restricted(cls, text: str) -> bool:
        return any(cmd in text for cmd in cls.RESTRICTED_COMMANDS)
