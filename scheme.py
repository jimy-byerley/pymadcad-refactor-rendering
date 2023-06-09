# NOTE replacing madcad.scheme, still providing the annotations functions, but they are no more functions but classes
# NOTE their appropriate display is choosen depending on the scene they are rendered in

@dataclass
class note_floating:
	position: vec3,
	text: str,
	...
	def scheme(self) -> Scheme:  ...
	def display(self, scene): ...

@dataclass
class note_label:
	axis: Axis,
	text: str,
	...
	def scheme(self) -> Scheme:  ...
	def display(self, scene): ...

@dataclass
class note_leading:
	axis: Axis,
	text: str,
	...
	def scheme(self) -> Scheme:  ...
	def display(self, scene): ...

@dataclass
class note_radius:
	surface: Mesh,
	text: str,
	...
	def scheme(self) -> Scheme:  ...
	def display(self, scene): ...

...  # NOTE and all other annotations functions currently in madcad.scheme
