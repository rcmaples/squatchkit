//

import * as Squatch from '../index'

describe('Squatch UI Components', () => {
  it('can be imported', () => {
    expect(typeof Squatch).toBe('object');
  });

  it('should export components', () => {
    expect(
      Object.keys(Squatch).sort())
      .toContain("Button")
  });

})