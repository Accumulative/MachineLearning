import Controller from '@ember/controller';
import Ember from 'ember';

export default Controller.extend({
  title: 'Multiple linear regression',
  image: '',
  ajax: Ember.inject.service(),
  graphs: [],
  actions: {
    execute() {
      this.get('ajax').request('/multiple_linear_regression').then(data => {
        this.set('graphs', data.data);
      });
    }
  }
});
