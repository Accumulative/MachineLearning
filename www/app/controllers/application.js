import Controller from '@ember/controller';

export default Controller.extend({
  title: 'Machine learning',
  navigation: Object.entries({
    'regression': ['simple linear regression', 'multiple linear regression'],
  }).reduce((total, [k, v]) => {
    total[k] = v.map(x => ({title: x.toLocaleUpperCase(), link: k + '/' + x.replace(/ /g, '-')}));
    return total;
  }, {})

});
