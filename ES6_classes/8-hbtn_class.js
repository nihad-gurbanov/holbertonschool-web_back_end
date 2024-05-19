export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') {
      throw TypeError('size must be number');
    }
    if (typeof location !== 'string') {
      throw TypeError('location must be string');
    }

    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') {
      return this._size;
    }
    if (hint === 'string' || hint === 'default') {
      return this._location;
    }
    return null;
  }
}
