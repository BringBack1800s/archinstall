from typing import TYPE_CHECKING, Any

from archinstall.default_profiles.profile import Profile, ProfileType

if TYPE_CHECKING:
	_: Any


class MinimalProfile(Profile):
	def __init__(self) -> None:
		super().__init__(
			'Minimal',
			ProfileType.Minimal,
			description=str(_('A very basic installation that allows you to customize Arch Linux as you see fit.'))
		)
