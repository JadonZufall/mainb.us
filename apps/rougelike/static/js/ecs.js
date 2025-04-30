const E_DamageTypes = {
	default: "Physical",
	0: "Physical",
};

class Entity {
	constructor() {
		this.id = '';
		this.components = new Map();
		this.destroyed = false;
	}

	_destroy() {
		this.destroy();
		this.destroyed = true;
		this.components.forEach(component => { component.destroy(); });
		this.components.clear();
	}

	destroy() {}

	_update() {
		this.update();
		this.components.forEach(component => { component._update(); });
	}

	update() {}

	addComponent(componentType, args={}) {
		if (this.hasComponent(componentType)) { throw new Error("Component already exists"); }
		this.components.set(componentType, new componentType(args));
		return this;
	}

	delComponent(componentType) {
		if (!this.hasComponent(componentType)) { throw new Error("Component does not exist"); }
		this.components.get(componentType)._destroy();
		this.components.delete(componentType);
		return this;
	}

	hasComponent(componentType) { return this.components.has(componentType); }
}

class Item extends Entity {
	constructor(args={}) {
		super(args);
		this.id = "item-";
	}
}


class Weapon extends Item {
	constructor(args={}) {
		super(args);
		this.id = "weapon-";
	}
}



class Actor extends Entity {
	constructor(args={}) {
		super();
		this.id = "actor-";

		this.addComponent(new Position2D());

		Object.hasOwn(args, "x") ? this.components.get(Position2D).position.x = args.x : null;
		Object.hasOwn(args, "y") ? this.components.get(Position2D).position.y = args.y : null;

		this.addComponent(new Name());
		Object.hasOwn(args, "name") ? this.components.get(Name).name = args.name : null;
	}
}

class Component {
	constructor() {
		this.parent = null;
		this.destroyed = false;
	}

	destroy() {}

	_destroy() {
		this.destroy();
		this.parent = null;
		this.destroyed = true;
	}
}

class Position2D extends Component {
	constructor() {
		super();
		this.position = { x: 0, y: 0 };
	}
}

class Name extends Component {
	constructor() {
		super();
		this.name = "{Name}";
	}
}

class BodyPart extends Component {
	constructor() {
		super();
	}
}


class Inventory extends Component {
	constructor() {
		super();
		this.items = {};
	}
}




