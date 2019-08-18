import Controller from '@ember/controller';
import Ember from 'ember';

export default Controller.extend({
  title: 'Multiple linear regression',
  image: '',
  ajax: Ember.inject.service(),
  graphs: [],
  table: [],
  actions: {
    execute() {
      this.get('ajax').request('/multiple_linear_regression').then(data => {
        this.set('graphs', data.data);
      });
    },
    backward_propagation() {
      this.get('ajax').request('/multiple_linear_regression/backward_propagation?sl=0.05').then(data => {
        this.set('table', data.data);
      });
    },
  }
});
