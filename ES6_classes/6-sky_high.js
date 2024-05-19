import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof sqft !== 'number') {
      throw TypeError('sqft must be a number');
    }
    if (typeof floors !== 'number') {
      throw TypeError('floors must be a number');
    }
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return super.sqft;
  }

  set sqft(value) {
    super.sqft = value;
  }

  get floors() {
    return this._floors;
  }

  set floors(value) {
    this._floors = value;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
