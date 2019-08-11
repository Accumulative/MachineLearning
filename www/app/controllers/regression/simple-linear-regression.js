import Controller from '@ember/controller';
import Ember from 'ember';

export default Controller.extend({
  title: 'Simple linear regression',
  image: '',
  ajax: Ember.inject.service(),
  one: '',
  two: '',
  actions: {
    execute() {
      this.get('ajax').request('/simple_linear_regression').then(data => {
        this.set('graphs', data.data);
      });
    }
  }
});
