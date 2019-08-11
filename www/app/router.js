import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('regression/simple-linear-regression');
  this.route('regression/multiple-linear-regression');
  this.route('home');
});

export default Router;
