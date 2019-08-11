import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | multiple-linear-regression', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:multiple-linear-regression');
    assert.ok(route);
  });
});
